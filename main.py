from crewai import Agent, Task, Crew, LLM
from crewai.knowledge.source.excel_knowledge_source import ExcelKnowledgeSource
from warnings import filterwarnings
from dotenv import load_dotenv
from crewai_tools import CodeInterpreterTool
import os

filterwarnings("ignore")
load_dotenv()

agent_llm = LLM(
    model=os.getenv("AGENT_MODEL_NAME"), api_key=os.getenv("OPENAI_API_KEY")
)

manager_llm = LLM(
    model=os.getenv("OLLAMA_MODEL_NAME"), base_url="http://127.0.0.1:11434"
)

excel_source = ExcelKnowledgeSource(file_paths=["capex.xlsx"])

code_interpreter = CodeInterpreterTool(unsafe_mode=True)

# Enhanced agent with memory and validation
data_analyst = Agent(
    role="Senior Financial Data Analyst specializing in CAPEX Analysis",
    goal="Extract actionable insights from financial data using Python analytics, identifying investment patterns, cost optimization opportunities, and strategic recommendations for capital expenditure decisions",
    backstory="""You are a seasoned financial analyst with 10+ years of experience at top-tier investment firms like JP Morgan.
    You specialize in capital expenditure analysis, having evaluated billions in corporate investments.
    Your expertise includes identifying spending patterns, ROI analysis, budget variance detection, and strategic cost optimization.
    You excel at translating complex financial data into clear, actionable business insights that drive executive decision-making.
    You always provide data-driven recommendations with supporting evidence and visualizations.""",
    llm=agent_llm,
    knowledge_sources=[excel_source],
    tools=[code_interpreter],
    reasoning=True,
    memory=True,  # Learn from past analyses
    max_reasoning_attempts=2,
    verbose=True,
)


data_analysis_task = Task(
    description=(
        "Perform comprehensive CAPEX analysis on the Excel data in your knowledge source based on user query: ({query}). "
        "Follow this analytical framework:\n"
        "1. **Data Understanding**: First examine the structure and contents of the CAPEX data\n"
        "2. **Query Analysis**: Interpret the user's specific question and requirements\n"
        "3. **Data Processing**: Clean, filter, and prepare data using pandas\n"
        "4. **Analysis**: Apply appropriate statistical and financial analysis methods\n"
        "5. **Insights**: Identify key patterns, trends, and anomalies\n"
        "6. **Recommendations**: Provide actionable business recommendations\n"
        "Always include:\n"
        "- Summary statistics and key metrics\n"
        "- Visual representations when helpful\n"
        "- Clear explanations of methodology\n"
        "- Business implications of findings\n"
        "- Specific recommendations with supporting rationale"
    ),
    expected_output="A comprehensive financial analysis report including data insights, visualizations, key findings, and strategic recommendations that directly address the user's query",
    agent=data_analyst,
)

crew = Crew(agents=[data_analyst], tasks=[data_analysis_task], verbose=True)

query = {"query": input("Enter your query: ")}

result = crew.kickoff(inputs=query)
print(result)
