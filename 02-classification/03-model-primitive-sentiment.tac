-- Model Primitive: Mocked Sentiment Classifier
--
-- Use a Model primitive when you want stateless, repeatable predictions.
-- This example uses a mock backend so it runs in CI without API keys.

Model "sentiment_mock" {
  type = "mock",
  value = {label = "positive", confidence = 0.93},
  input = {text = "string"},
  output = {label = "string", confidence = "float"}
}

Procedure {
  input = {
    text = field.string{required = true, description = "Text to classify"}
  },
  output = {
    label = field.string{required = true, description = "Sentiment label"},
    confidence = field.number{required = true, description = "Confidence score"}
  },
  function(input)
    local classifier = Model("sentiment_mock")
    local result = classifier({text = input.text})
    local output = result.output or result

    return {label = output.label, confidence = output.confidence}
  end
}

Specification([[
Feature: Model primitive (mocked sentiment)

  Scenario: Returns the mocked label and confidence
    Given the procedure has started
    And the input text is "This product is wonderful."
    When the procedure runs
    Then the procedure should complete successfully
    And the output label should be "positive"
    And the output confidence should be 0.93
]])
