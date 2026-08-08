

# Nuestro Generalizable Face AuthenticationCNN (GFA-CNN) está disponible en: https://arxiv.org/abs/1901.05602 
Este proyecto fue creado por Tu Xiaoguang (xguangtu@outlook.com) 

Para facilitar la investigación en la comunidad de anti-spoofing facial, publicamos nuestro código de prueba (incluido el modelo) para GFA-CNN; el código de entrenamiento estará disponible una vez aceptado nuestro artículo.  

# Agregamos los códigos para FDA en la carpeta "FDA_codes"
Uso: Tensorflow-1.12.0, python-2.7 // Descargue el paquete "fda_model.rar" en: https://pan.baidu.com/s/1P3_BrVkc0A4Y9wtL72PiAg usando la contraseña: "39lk". Coloque el paquete en la carpeta "FDA_codes/scripts", extraígalo y luego escriba los siguientes comandos en la terminal (es posible que deba modificar la ruta en el script "evaluate_inFolder_mfsdPhoto.py" y los archivos txt de etiquetas de prueba): 

python evaluate_inFolder_mfsdPhoto.py --allow-different-dimensions --checkpoint fda_model/mfsdPhotoAtck/fns.ckpt --in-path content --out-path outputs/

# Referencia
Si encuentras nuestro código útil para tu investigación, por favor cita nuestro trabajo:

@article{tu2019learning,
  title={Learning Generalizable and Identity-Discriminative Representations for Face Anti-Spoofing},
  author={Tu, Xiaoguang and Zhao, Jian and Xie, Mei and Du, Guodong and Zhang, Hengsheng and Li, Jianshu and Ma, Zheng and Feng, Jiashi},
  journal={arXiv preprint arXiv:1901.05602},
  year={2019}
}
