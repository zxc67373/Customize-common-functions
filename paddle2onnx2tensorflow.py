import os
try:
    os.system('paddle2onnx --model_dir ch_PP-OCRv3_rec_infer --model_filename inference.pdmodel --params_filename inference.pdiparams --save_file ./onnx_model/rec_large.onnx --opset_version 11 --enable_onnx_checker True')
    os.system('onnx-tf convert -t tf -i onnx_model/rec_large.onnx -o OCRv3.pb')
except:
    os.system('pip install onnx ')
    os.system('pip install tensorflow ')
    os.system('paddle2onnx --model_dir ch_PP-OCRv3_rec_infer --model_filename inference.pdmodel --params_filename inference.pdiparams --save_file ./onnx_model/rec_large.onnx --opset_version 11 --enable_onnx_checker True')
    os.system('onnx-tf convert -t tf -i onnx_model/rec_large.onnx -o OCRv3.pb')
