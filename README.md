# Diabetic Retinopathy Diagnosis
Diabetic Retinopathy (DR) is a complication of diabetes that damages the retina and is a leading cause of blindness. It affects up to 80% of individuals who have had diabetes for 20 years or more, often without early warning signs. Retinal (fundus) photography, interpreted manually, is a widely accepted and effective screening tool for DR, sometimes outperforming in-person dilated eye exams. The below figure shows an example of a healthy patient and a patient with diabetic retinopathy as viewed by fundus photography (source):
<p align="center">
  <img src="https://github.com/user-attachments/assets/c9c869c1-be1c-41a7-ae13-187c84be9714" alt="Diabetic Retinopathy Example"/>
</p>

This project aims to develop a deep learning model, specifically using the VGG16 architecture, to automatically classify diabetic retinopathy severity from retinal images. The model assigns a score based on the following scale:

0: No DR \
1: Mild DR \
2: Moderate DR \
3: Severe DR \
4: Proliferative DR \
![image](https://github.com/user-attachments/assets/25744839-c665-40ee-8b13-4755af95160f)
