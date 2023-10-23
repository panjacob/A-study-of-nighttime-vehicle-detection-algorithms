import onnx

onnx_model_path = 'n50_50_100.onnx'
tf_model_path = 'tfpath'

onnx_model = onnx.load(onnx_model_path)

from onnx_tf.backend import prepare

tf_rep = prepare(onnx_model)

tf_rep.export_graph(tf_model_path)