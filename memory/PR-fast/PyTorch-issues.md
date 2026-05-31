
## PyTorch Good First Issues (from subagent search)
1. Use typing_extensions.TypeAliasType for better reexport of __module__ (#171905) - module: typing
2. torch.compile regression 2.9.1: Triton kernel name not defined - module: inductor
3. [auto functionalize][partitioner] ones_like not getting recomputed - oncall: export
4. [dynamo][dynamic] torch.combinations throws RuntimeError with aot_eager+dynamic - module: dynamic shapes
5. foreach_map enhancements - module: inductor, dynamo
6. Make tlparse able to show summary of distinct graph breaks - module: dynamo
7. [Feature] torch.export .save/.load could support safetensors/weights_only=True - oncall: export
8. aten.grid_sampler_3d.default missing c-shm implementation - module: inductor
9. [BUG][quant] get_source_partitions() may return different matches - oncall: quantization
10. Improve error message for wrong number of args in CachingAutotuner - module: error checking

