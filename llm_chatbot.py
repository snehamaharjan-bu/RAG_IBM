from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM
import gradio as gr

# Model and project settings
#model_id = 'mistralai/mistral-small-3-1-24b-instruct-2503' # Specify the Mixtral 8x7B model
model_id = 'ibm/granite-3-3-8b-instruct' # Specify IBM's Granite 3.3 8B model

# Set necessary parameters for model setup
parameters = {
    GenParams.MAX_NEW_TOKENS: 350,  # Specify the max tokens you want to generate in the response
    GenParams.TEMPERATURE: 0.75, # This randomness or creativity of the model's responses
}

project_id = "skills-network" #for cloud IDE setup

# Wrap up the model into WatsonxLLM inference
watsonx_llm = WatsonxLLM(
    model_id=model_id,
    url="https://us-south.ml.cloud.ibm.com",
    project_id=project_id,
    params=parameters,
)

# Function to generate a response from the model based on prompt input
def generate_response(prompt_txt):
    generated_response = watsonx_llm.invoke(prompt_txt)
    return generated_response

# Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Enter your questions here"),
    outputs=gr.Textbox(label="Output",lines=10),
    title="Sneha's Watsonx.ai Chatbot",
    description="Ask any question to the chatbot here"
)

# Launch the app
chat_application.launch(server_name="127.0.0.1", server_port= 7960, share=True)