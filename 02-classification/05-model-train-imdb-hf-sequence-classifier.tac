-- Trainable Model Primitive: Hugging Face Sequence Classifier on IMDB
--
-- This example uses the Hugging Face Trainer API under the hood
-- (AutoModelForSequenceClassification) and registers the trained artifact.
--
-- Key idea: your Procedure logic is the same regardless of backend.
-- In CI we test deterministically with mocks; real training is optional.
--
-- Install HF extras (required for real training/inference):
--   pip install tactus[hf]
--
-- Train:
--   tactus train 02-classification/05-model-train-imdb-hf-sequence-classifier.tac --model imdb_hf
--
-- Evaluate:
--   tactus models evaluate 02-classification/05-model-train-imdb-hf-sequence-classifier.tac --model imdb_hf
--
-- Test mocked (CI-safe):
--   tactus test 02-classification/05-model-train-imdb-hf-sequence-classifier.tac --mock
--
-- Test real (requires you trained first):
--   tactus test 02-classification/05-model-train-imdb-hf-sequence-classifier.tac
--
-- Notes:
-- - HF training can use GPU automatically when available.
-- - To force CPU, set `training_args = { no_cuda = true }` in hyperparameters.

Model "imdb_hf" {
  type = "registry",
  name = "imdb_hf",
  version = "latest",

  input = { text = "string" },
  output = { label = "string", confidence = "float" },

  training = {
    data = {
      source = "hf",
      name = "imdb",
      train = "train",
      test = "test",
      shuffle = { train = true, test = true },
      -- Keep the default small so it is approachable on CPU.
      -- Increase these limits for better accuracy (and longer training time).
      limit = { train = 2000, test = 1000 },
      seed = 42,
      text_field = "text",
      label_field = "label"
    },
    candidates = {
      {
        name = "hf-distilbert",
        trainer = "hf_sequence_classifier",
        hyperparameters = {
          model = "distilbert-base-uncased",
          labels = {"negative", "positive"},
          epochs = 1,
          batch_size = 8,
          learning_rate = 2e-5,
          max_length = 256,
          padding = "max_length",
          truncation = true,
          training_args = {
            evaluation_strategy = "no",
            save_strategy = "no",
            logging_steps = 50
          }
        }
      }
    }
  }
}

Procedure {
  input = {
    text = field.string{
      required = true,
      description = "A movie review to classify as positive/negative"
    }
  },
  output = {
    label = field.string{required = true},
    confidence = field.number{required = false},
    decision = field.string{required = true}
  },
  function(input)
    local classifier = Model("imdb_hf")
    local result = classifier({text = input.text})
    local output = result.output or result

    local decision = "review"
    if output.confidence ~= nil and output.confidence >= 0.7 then
      if output.label == "positive" then
        decision = "yes"
      else
        decision = "no"
      end
    end

    return {
      label = output.label,
      confidence = output.confidence,
      decision = decision
    }
  end
}

Mocks {
  imdb_hf = {
    conditional = {
      {
        when = {text = "A wonderful movie with great acting."},
        returns = {label = "positive", confidence = 0.91}
      },
      {
        when = {text = "This was a terrible movie with bad acting."},
        returns = {label = "negative", confidence = 0.88}
      },
      {
        when = {text = "A confusing movie with uneven pacing."},
        returns = {label = "positive", confidence = 0.49}
      }
    }
  }
}

Specification([[
Feature: Trainable Model primitive (HF sequence classifier IMDB)

  Scenario: Positive review routes to yes
    Given the procedure has started
    And the input text is "A wonderful movie with great acting."
    When the procedure runs
    Then the output decision should be "yes"
    And the output label should be "positive"
    And the procedure should complete successfully

  Scenario: Negative review routes to no
    Given the procedure has started
    And the input text is "This was a terrible movie with bad acting."
    When the procedure runs
    Then the output decision should be "no"
    And the output label should be "negative"
    And the procedure should complete successfully

  Scenario: Low confidence routes to review
    Given the procedure has started
    And the input text is "A confusing movie with uneven pacing."
    When the procedure runs
    Then the output decision should be "review"
    And the output confidence should exist
    And the procedure should complete successfully
]])

