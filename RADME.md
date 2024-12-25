# SAT Analyzer

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Arguments](#command-line-arguments)
  - [Examples](#examples)
- [Output](#output)
  - [CSV Files](#csv-files)
  - [Plots](#plots)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview

**SAT Analyzer** is a comprehensive tool designed to solve and analyze Boolean satisfiability problems (SAT) and their 3-CNF variants (3SAT). It provides functionalities for:

- Solving SAT and 3SAT instances using customizable algorithms.
- Reducing SAT problems to 3SAT.
- Generating random SAT and 3SAT instances.
- Profiling solver performance in terms of execution time and memory usage.
- Visualizing analysis results through plots.
- Saving analysis data to CSV files.
- Providing a user-friendly Command-Line Interface (CLI) with real-time progress feedback.

Whether you're a researcher, student, or enthusiast in computational logic and algorithm analysis, SAT Analyzer offers the tools you need to explore and evaluate SAT-solving strategies effectively.

## Features

- **Multiple Algorithms**: Choose between SAT, 3SAT, or SAT-to-3SAT reduction algorithms.
- **Instance Generation**: Generate random SAT or 3SAT instances with customizable parameters.
- **Performance Profiling**: Measure execution time and memory consumption of solvers.
- **Data Visualization**: Plot analysis results to visualize performance trends.
- **Data Export**: Save analysis data to CSV files for further examination or reporting.
- **Progress Feedback**: Real-time progress indicators using `tqdm` for enhanced CLI experience.
- **Flexible Configuration**: Customize various parameters through command-line arguments.

## Installation

### Prerequisites

- **Python 3.7 or higher**: Ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/yourusername/sat-analyzer.git
cd sat-analyzer
```

### Install Dependencies
It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

SAT Analyzer is executed via the command line. Below are the available options and examples to help you get started.

### Command-Line Arguments

| Argument          | Short Flag | Description                                        | Default |
|-------------------|------------|----------------------------------------------------|---------|
| `-a`, `--algo`    | `-a`       | Select an algorithm `[SAT, 3SAT, SAT-2-3SAT]`       | `SAT`   |
| `-f`, `--file`    | `-f`       | Cluster input file (not implemented in this version) | `None` |
| `-n`, `--analyser`| `-n`      | Select an analyser `[TIME, MEMORY]`                | `TIME`  |
| `-t`, `--test`    | `-t`       | Generate N tests (overrides file input)            | `0`     |
| `-g`, `--graph`   | `-g`       | Enable graph generation for analysis output        | `False` |
| `-v`, `--vars`    | `-v`       | Number of variables for random instance generation  | `3`     |
| `-c`, `--clauses` | `-c`       | Number of clauses for random instance generation    | `3`     |
| `-mn`, `--min`    | `-mn`      | Minimum size of cluster                             | `1`     |
| `-mx`, `--max`    | `-mx`      | Maximum size of cluster                             | `3`     |


### Examples
1. Basic SAT Solver with Default Setting
    ```bash
    python main.py
    ```
2. 3SAT Solver with Memory Analysis
    ```bash
    python main.py -a 3SAT -n MEMORY
    ```
3. Generate 50 Random SAT Instances and Plot Execution Time
    ```bash
    python main.py -a SAT -n TIME -t 50 -g
    ```

4. Reduce SAT to 3SAT and Analyze Memory Usage
    ```bash
    python main.py -a SAT-2-3SAT -n MEMORY
    ```

5. Specify Number of Variables and Clauses
    ```bash
    python main.py -v 10 -c 20
    ```

## Output

### CSV Files
After running tests, analysis data is saved to CSV files located in the output/ directory. The filename follows the pattern:

```bash
<Algorithm>_<Analyser>_analysis.csv
```

### Plots

If the graph option is enabled (-g flag), the script generates plots visualizing the analysis results. Testing flag must be also setted (-t flag)! 


Plots display:

- **X-Axis**: Number of Clauses.
- **Y-Axis**: Execution Time (s) or Memory Consumption (MB).

```python
python main.py -t 10 -g true
```