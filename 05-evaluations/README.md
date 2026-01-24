# Evaluations

This chapter explores Tactus evaluations - quantitative assessments of AI workflow performance across datasets.

## What You'll Learn

- Defining evaluation criteria and metrics
- Running evaluations over test datasets
- Success rate calculations and thresholds
- Trace-based evaluations for debugging
- Dataset management (JSONL format)
- Statistical analysis of evaluation results
- Comparing different models and prompts

## Examples

_Examples coming soon. This chapter will cover evaluation patterns for measuring and improving AI workflow quality._

## Key Concepts

**Evaluation**: Quantitative assessment that runs a procedure multiple times and aggregates results. Defined with `Evaluation([[...]])` blocks.

**Metrics**: Numerical measures of performance like success rate, accuracy, precision, recall. Evaluations can track multiple metrics simultaneously.

**Datasets**: Collections of test cases in JSONL format. Each line contains input parameters and optionally expected outputs.

**Thresholds**: Minimum acceptable metric values. Evaluations can be configured to fail if metrics don't meet thresholds (e.g., success_rate >= 0.95).

**Traces**: Detailed execution logs for each evaluation run. Useful for debugging why particular test cases fail.

**Success Criteria**: Conditions that determine whether an evaluation run succeeds. Can be based on exact matches, fuzzy matching, or custom logic.
