# Data Analysis Agent

An intelligent AI-powered financial data analysis agent built with CrewAI that performs comprehensive CAPEX (Capital Expenditure) analysis using Python and pandas. This project demonstrates how to create autonomous agents capable of analyzing Excel spreadsheets and providing actionable financial insights.

## Features

- 🤖 **AI-Powered Analysis**: Uses advanced language models (OpenAI and Ollama) for intelligent data interpretation
- 📊 **Excel Integration**: Seamlessly reads and analyzes Excel files using CrewAI's knowledge sources
- 🐍 **Python Code Execution**: Executes Python pandas operations dynamically for data manipulation and analysis
- 💼 **Financial Focus**: Specifically designed for CAPEX analysis with expertise in investment decision-making
- 🧠 **Memory & Reasoning**: Learns from past analyses and applies sophisticated reasoning
- 📈 **Comprehensive Reporting**: Generates detailed analysis reports with visualizations and strategic recommendations
- 🔍 **Interactive Queries**: Accepts custom user queries for targeted analysis

## Architecture

The project uses a multi-agent architecture powered by CrewAI:

- **Senior Financial Data Analyst Agent**: An experienced analyst with 10+ years of investment firm experience
- **Code Interpreter Tool**: Executes Python code for data analysis and visualization
- **Excel Knowledge Source**: Processes and understands Excel data files
- **Dual LLM Setup**: Combines OpenAI for agent operations and local Ollama models for management
- **Memory System**: Retains insights from previous analyses for improved performance

## Prerequisites

- Python 3.8+
- OpenAI API key
- Ollama installed locally (running on port 11434)
- Excel files with CAPEX data

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd data-analysis-agent
```

2. Install dependencies using uv (recommended) or pip:

```bash
# Using uv
uv sync

# Or using pip
pip install crewai crewai-tools ollama pandas python-dotenv openpyxl
```

3. Set up environment variables:
   Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
AGENT_MODEL_NAME=gpt-4
OLLAMA_MODEL_NAME=llama3.2
```

4. Start Ollama locally:

```bash
ollama serve
```

5. Make sure you have the required Ollama model:

```bash
ollama pull llama3.2
```

## Usage

1. Place your Excel files in the `knowledge/` directory (e.g., `knowledge/capex.xlsx`)

2. Run the analysis:

```bash
python main.py
```

3. Enter your query when prompted (examples below)

4. The agent will:
   - Load and analyze your Excel data
   - Execute Python pandas operations
   - Generate visualizations
   - Provide comprehensive insights and recommendations

## Example Queries

- "What are the top 5 categories by total CAPEX spend?"
- "Analyze spending trends over time and identify any anomalies"
- "Compare budget vs actual spending and highlight variances"
- "Which departments are over/under budget and by how much?"
- "Identify cost optimization opportunities in our CAPEX portfolio"
- "What's the ROI analysis for major capital investments?"

## Analytical Framework

The agent follows a structured approach:

1. **Data Understanding**: Examines structure and contents of CAPEX data
2. **Query Analysis**: Interprets specific user requirements
3. **Data Processing**: Cleans, filters, and prepares data using pandas
4. **Analysis**: Applies statistical and financial analysis methods
5. **Insights**: Identifies patterns, trends, and anomalies
6. **Recommendations**: Provides actionable business recommendations

## Output Format

Each analysis includes:

- 📊 Summary statistics and key metrics
- 📈 Visual representations and charts
- 🔍 Clear explanations of methodology
- 💡 Business implications of findings
- 🎯 Specific recommendations with supporting rationale

## Project Structure

```
data-analysis-agent/
├── README.md              # This file
├── main.py                # Main application entry point
├── pyproject.toml         # Project dependencies
├── uv.lock               # Lock file for dependencies
├── .env                  # Environment variables (create this)
├── knowledge/            # Data files directory
│   └── capex.xlsx       # Sample CAPEX data
└── .venv/               # Virtual environment
```

## Configuration

The agent can be customized by modifying `main.py`:

- **LLM Models**: Change `AGENT_MODEL_NAME` and `OLLAMA_MODEL_NAME` in `.env`
- **Data Sources**: Add more Excel files to the `knowledge/` directory
- **Agent Behavior**: Modify the agent's role, goal, and backstory
- **Analysis Framework**: Adjust the task description for different analytical approaches

## Troubleshooting

### Common Issues:

1. **File Not Found Error**: Ensure Excel files are in the `knowledge/` directory
2. **API Key Issues**: Verify your OpenAI API key is set correctly in `.env`
3. **Ollama Connection**: Make sure Ollama is running on `http://127.0.0.1:11434`
4. **Model Not Found**: Pull the required Ollama model using `ollama pull <model-name>`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add your license here]

## Acknowledgments

- Built with [CrewAI](https://github.com/joaomdmoura/crewAI)
- Powered by OpenAI and Ollama
- Financial analysis expertise inspired by industry best practices

---

**Note**: This agent is designed for financial analysis and should be used in conjunction with human expertise for critical business decisions.
