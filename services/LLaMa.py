from transformers import (AutoTokenizer, AutoModelForCausalLM, pipeline)
from data.data import process_params, proposal_params
from services.services import clean_text

def load_model_and_tokenizer(model_path, device="cpu"):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    tokenizer.pad_token = tokenizer.eos_token 
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device)
    return model, tokenizer

def set_pipeline(model_path, pipeline_type):
    model, tokenizer = load_model_and_tokenizer(model_path)
    text_generator = pipeline(
        pipeline_type, model=model, tokenizer=tokenizer
    )
    return text_generator

def first_prompt(user_input, prompt_template=None):
    usr_input = clean_text(user_input)
    
    if prompt_template:
        prompt = prompt_template.format(user_input=usr_input)
    else:
        prompt = (
            f"Con base en la siguiente descripción: {usr_input}\n"
            f"Identifica lo siguiente:\n"
            f"1. Los procesos que se mencionan en la descripción.\n"
            f"2. Los roles que participan en cada proceso.\n"
            f"3. Las actividades específicas que desempeña cada rol.\n"
            f"4. Envía los resultados únicamente en el formato: <Proceso>, <Rol>, <Actividad>.\n"
            f"5. Elimina las redundancias.\n"
        )
    return prompt

def second_prompt(structured_data, prompt_template=None):
    if prompt_template:
        prompt = prompt_template.format(user_input=structured_data)
    else:
        prompt = (
            f"En base a la descripcion estructurada en formato <Proceso>,<Rol>,<Actividad>: {structured_data}\n"
            f"1. Propone un software para automatizar las actividades identificadas.\n"
            f"2. Detalla minuciosamente como será el nuevo roadmap del usuario en el software propuesto por cada actividad identificada.\n"
            f"3. Transforma cada uno de los pasos de los roadmaps a historias de usuario en formato Connextra.\n"
        )
    return prompt

def generate_response(generator, prompt, ptemperature, ptop_k, ptop_p, pmax_new_tokens, plength_penalty):
    inputs = generator.tokenizer(prompt, return_tensors="pt", padding=True)
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    outputs = generator.model.generate(
        input_ids = input_ids,
        attention_mask = attention_mask,
        num_return_sequences = 1,
        temperature = ptemperature,
        top_k = ptop_k,
        top_p = ptop_p,
        max_new_tokens = pmax_new_tokens,
        length_penalty = plength_penalty
    )

    decoded_output = generator.tokenizer.decode(outputs[0], skip_special_tokens=True)
    return decoded_output

def chat_llm(user_input, generator, prompt_template, process_params, proposal_params):
    prompt = first_prompt(user_input, prompt_template)
    structured_data = generate_response(
        generator, prompt, 
        process_params["temperature"], process_params["top_k"], process_params["top_p"], 
        process_params["max_new_tokens"], process_params["length_penalty"]
    )

    software_prompt = second_prompt(structured_data, prompt_template)
    software_proposal = generate_response(
        generator, software_prompt, 
        proposal_params["temperature"], proposal_params["top_k"], proposal_params["top_p"], 
        proposal_params["max_new_tokens"], proposal_params["length_penalty"]
    )

    return software_proposal

def generate_llm_response(user_input):
    model_path = "C:/Users/PC/Documents/LLaMa/Llama-3.1-8B-Instruct"
    pipeline_type = "text-generation"
    device = "cpu"
    prompt_template = None
    generator = set_pipeline(model_path, pipeline_type)
    software_proposal = chat_llm(user_input, generator, prompt_template, process_params, proposal_params)
    return software_proposal


