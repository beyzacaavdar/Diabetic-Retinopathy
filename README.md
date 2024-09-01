# Diabetic Retinopathy Diagnosis
Diabetic Retinopathy (DR) is a complication of diabetes that damages the retina and is a leading cause of blindness. It affects up to 80% of individuals who have had diabetes for 20 years or more, often without early warning signs. Retinal (fundus) photography, interpreted manually, is a widely accepted and effective screening tool for DR, sometimes outperforming in-person dilated eye exams. The below figure shows an example of a healthy patient and a patient with diabetic retinopathy as viewed by fundus photography:
<p align="center">
  <img src="https://github.com/user-attachments/assets/c9c869c1-be1c-41a7-ae13-187c84be9714" alt="Diabetic Retinopathy Example" alt="image" width="370"/>
</p>

This project aims to develop a deep learning model, specifically using the VGG16 architecture, to automatically classify diabetic retinopathy severity from retinal images. The model assigns a score based on the following scale:

0: No DR \
1: Mild DR \
2: Moderate DR \
3: Severe DR \
4: Proliferative DR 
<p align="center">
<img src="https://github.com/user-attachments/assets/25744839-c665-40ee-8b13-4755af95160f" alt="image" width="700"/>
</p>

# • Quick Start
If you want to use the app on google colab, you should clone the repo: 
```bash
!git clone https://github.com/beyzacaavdar/Diabetic-Retinopathy.git 
```
Set up a secure tunnel to expose a local web server to the internet using cloudflared tool: 
```bash
!wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 
!chmod +x cloudflared-linux-amd64 
!nohup /content/cloudflared-linux-amd64 tunnel --url http://localhost:8501 & 
```

Run the app.py and get the url to enter into the app: 
```bash
!streamlit run app.py &>/content/logs.txt & 
!grep -o 'https://.*\.trycloudflare.com' /content/nohup.out | head -n 1 | xargs -I {} echo "Your tunnel url {}" 
```
