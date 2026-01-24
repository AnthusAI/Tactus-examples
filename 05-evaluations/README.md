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

### 01-simple-eval.tac

A basic evaluation demonstrating core concepts without requiring LLM API calls. This example shows:
- Defining inline datasets with test cases
- Evaluation syntax with `Evaluation({...})`
- Expected output validation
- Success criteria based on exact output matching
- Running evaluations with `tactus eval`

This example uses a pure logic procedure (no LLM calls) to focus on evaluation mechanics - perfect for learning the evaluation framework without API costs.

### 02-success-rate.tac

Demonstrates success rate calculations and aggregated metrics. This example shows:
- Running multiple test cases in a single evaluation
- Calculating success rate across dataset
- Pass/fail criteria for individual test cases
- Aggregated statistics and reporting
- Using success rate to measure overall quality

Success rate is the primary metric for evaluating AI workflows - it tells you what percentage of test cases produce correct outputs.

### 03-thresholds.tac

Shows how to set minimum acceptable thresholds for metrics. This example demonstrates:
- Defining threshold requirements (e.g., success_rate >= 0.95)
- Evaluation failure when thresholds aren't met
- Multiple threshold configurations
- Using thresholds for quality gates in CI/CD
- Balancing strictness with practical tolerance

Thresholds are essential for automated quality control - they let you enforce minimum standards and catch regressions before deployment.

## Key Concepts

**Evaluation**: Quantitative assessment that runs a procedure multiple times and aggregates results. Defined with `Evaluation([[...]])` blocks.

**Metrics**: Numerical measures of performance like success rate, accuracy, precision, recall. Evaluations can track multiple metrics simultaneously.

**Datasets**: Collections of test cases in JSONL format. Each line contains input parameters and optionally expected outputs.

**Thresholds**: Minimum acceptable metric values. Evaluations can be configured to fail if metrics don't meet thresholds (e.g., success_rate >= 0.95).

**Traces**: Detailed execution logs for each evaluation run. Useful for debugging why particular test cases fail.

**Success Criteria**: Conditions that determine whether an evaluation run succeeds. Can be based on exact matches, fuzzy matching, or custom logic.
