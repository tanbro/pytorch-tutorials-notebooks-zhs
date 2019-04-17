# pytorch-tutorials-notebooks-zhs

[PyTorch tutorials](https://github.com/pytorch/tutorials/)的中文翻译。

官方教程以*带有Sphinx-Doc扩展rST格式注释的Python源代码*的形式制作了Web文档并导出 Jupyter Notebook。

而这个项目除了翻译，修改还有:

- 使用 Jupyter Notebook 保存说明和代码片段
- 由 Jupyter Notebook 导出Markdown文件，并在其基础上构建Web文档

这是个人的翻译笔记，用于个人学习 PyTorch。

目前只翻译和转换了部分 `*.py`文件(用 Sphinx-Gallery 制作了 Jupyter Notebook) ，没有处理任何 `*.rst`(单纯的 Sphinx-Doc 文档)

## 目录

- 准备开始
  - 用 PyTorch 进行深度学习：60分钟闪电战
    - 

## Env

准备一个 Python3.6 环境，我们使用 conda 管理环境:

```console
(base) user@host:~$ conda create --name pytorch-tutorials --python=3.6
(base) user@host:~$ conda activate pytorch-tutorials
(pytorch-tutorials) user@host:~$ conda install -y ipykernel
(pytorch-tutorials) user@host:~$ python -m ipykernel install --user --name pytorch-tutorials --display-name "pytorch-tutorials"
(pytorch-tutorials) user@host:~$ conda install -y pytorch torchvision cudatoolkit=9.0 -c pytorch
(pytorch-tutorials) user@host:~$ conda install -y tensorflow-gpu
(pytorch-tutorials) user@host:~$ conda install -y -c conda-forge pandas matplotlib scikit-learn scikit-image tqdm
```
