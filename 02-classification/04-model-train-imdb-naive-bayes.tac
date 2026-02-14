-- Trainable Model Primitive: Naive Bayes sentiment on IMDB
--
-- This example demonstrates the full "Model lifecycle" in one file:
-- - Declare a registry-backed Model with an explicit training configuration
-- - Use the Model inside a Procedure (your code branches on model output)
-- - Test deterministically with Mocks (CI-safe)
-- - Optionally train + evaluate the real model and run the same Procedure/specs
--
-- Install ML extras (required for real training/inference):
--   pip install tactus[ml]
--
-- Train (writes a version to the registry):
--   tactus train 02-classification/04-model-train-imdb-naive-bayes.tac --model imdb_nb
--
-- Evaluate (optional; compares registered versions/tags against the test split):
--   tactus models evaluate 02-classification/04-model-train-imdb-naive-bayes.tac --model imdb_nb
--
-- Test in mock mode (fast, deterministic, no downloads):
--   tactus test 02-classification/04-model-train-imdb-naive-bayes.tac --mock
--
-- Test in real mode (requires you trained the model first):
--   tactus test 02-classification/04-model-train-imdb-naive-bayes.tac

Model "imdb_nb" {
  type = "registry",
  name = "imdb_nb",
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
      limit = { train = 25000, test = 25000 },
      seed = 42,
      text_field = "text",
      label_field = "label"
    },
    candidates = {
      {
        name = "nb-tfidf",
        trainer = "naive_bayes",
        hyperparameters = {
          alpha = 1.0,
          max_features = 50000,
          ngram_min = 1,
          ngram_max = 2
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
    decision = field.string{
      required = true,
      description = "yes | no | review (a simple policy driven by the model output)"
    }
  },
  function(input)
    local classifier = Model("imdb_nb")
    local result = classifier({text = input.text})
    local output = result.output or result

    -- This is the point of the example: your procedure stays deterministic,
    -- and you use the model's output as a signal that drives policy.
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

-- Deterministic model responses for CI-safe specs.
Mocks {
  imdb_nb = {
    conditional = {
      {
        when = {text = "A wonderful movie with great acting."},
        returns = {label = "positive", confidence = 0.92}
      },
      {
        when = {text = "This was a terrible movie with bad acting."},
        returns = {label = "negative", confidence = 0.87}
      },
      {
        when = {text = "A confusing movie with uneven pacing."},
        returns = {label = "positive", confidence = 0.42}
      }
    }
  }
}

Specification([[
Feature: Trainable Model primitive (Naive Bayes IMDB)

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

