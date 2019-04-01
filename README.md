# GFA-CNN
# Our Generalizable Face AuthenticationCNN (GFA-CNN) is available at: https://arxiv.org/abs/1901.05602 

# We add the codes for FDA in the folder "FDA_codes"
Usage: Tensorflow-1.12.0, python-2.7 // Download the "fda_model.rar" package at： https://pan.baidu.com/s/1P3_BrVkc0A4Y9wtL72PiAg using the password: "39lk". Putting the package under the folder "FDA_codes/scripts", extracting it and then type the flowing  commond in the terminal:
python evaluate_inFolder_mfsdPhoto.py --allow-different-dimensions --checkpoint fda_model/mfsdPhotoAtck/fns.ckpt --in-path content --out-path outputs/
