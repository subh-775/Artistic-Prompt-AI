<p align="center">
    <img src="https://readme-typing-svg.demolab.com/?lines=🚀%20Teaching%20Diffusion%20Models%20to%20Write;&font=Fira%20Code&align=center&width=1000&height=80&color=f2m358&vCenter=true&pause=2000&size=40" />
</p>

<h1 align="center">🎨 AI-Powered Poster Generator</h1>

## 🌟 **Introduction**

We've designed a machine learning model capable of generating images that **accurately incorporate specified text or lettering within the image**. Existing image-generation models often struggle with proper text placement, either misplacing the text or introducing spelling errors. Our goal is to train the model to master the art of **placing text accurately and aesthetically within generated images**. This innovation enables the seamless creation of visually appealing outputs such as **poster designs** and **template fills**, all from a single prompt.

---

## 🚀 **Motivation**
Despite the progress in AI image generation, no model has mastered the art of text placement. Challenges we aim to solve:
- Ensuring **precise text placement** that enhances the visual appeal.
- Preventing **spelling errors** and maintaining stylistic consistency.
- Supporting **unstructured text** in different layouts and styles.

Our project brings together advanced AI techniques and innovative approaches to overcome these limitations.

---

## ⚙️ **How It Works**

### **1. Image Generation**
We used **[`black-forest-labs/FLUX.1-dev`](https://huggingface.co/black-forest-labs/FLUX.1-dev)** for generating high-quality images. This model serves as the backbone of our pipeline.

### **2. Conditional Image Control**
Using **[`ControlNet`](https://github.com/lllyasviel/ControlNet)**, we ensure the model adheres to layout constraints like text placement, image structure, and artistic styling.

### **3. Data Preparation**
- **Poster Collection**: Thousands of poster images were collected and cleaned.
- **Caption Generation**: Leveraged **[`moondream2`](https://huggingface.co/vikhyatk/moondream2)** to create captions describing each poster.
- **Conditional Images**: Created lineart images with **[`ControlNet-v1-1-nightly`](https://github.com/lllyasviel/ControlNet-v1-1-nightly/blob/main/README.md#controlnet-11-lineart)** for layout guidance.

| **🖼️ Image**        | **✍️ Caption**                                                             | **🖊️ Conditional Image**     |
|----------------------|---------------------------------------------------------------------------|-------------------------------|
| Movie poster image   | A description of the poster, including characters, text, colors, etc.    | Lineart representation        |

- **Dataset Link**: [ControlNet-Poster Dataset](https://huggingface.co/datasets/fhai50032/ControlNet-Poster)

---

## 🧠 **Model Training**

### **Training Pipeline**
We trained the model using the following parameters:

```python
!accelerate launch train_controlnet_flux.py \
    --pretrained_model_name_or_path="black-forest-labs/FLUX.1-dev" \
    --dataset_name="fhai50032/ControlNet-Poster" \
    --conditioning_image_column="conditional_image" \
    --image_column="image" \
    --caption_column="caption" \
    --output_dir="text-controlnet" \
    --mixed_precision="bf16" \
    --resolution=512 \
    --learning_rate=3e-5 \
    --max_train_steps=3000 \
    --train_batch_size=2 \
    --gradient_accumulation_steps=3 \
    --report_to="wandb" \
    --num_double_layers=4 \
    --num_single_layers=2 \
    --seed=42 \
    --lr_scheduler "cosine" \
    --checkpointing_steps 100 \
    --max_train_samples 3000 \
    --use_adafactor \
    --push_to_hub
```
## Training Highlights
- **Hardware:** Trained on an **NVIDIA A100** GPU
### **📉 Loss Graph**
- Loss Functions:
- MSE (Mean Squared Error)
- NLL (Negative Log-Likelihood)
- 🔵 Previous loss
- 🟢 New loss 
![Loss Graph](test_imgs/loss.jpg)

### **🧭 Learning Rate**
The learning rate progression during training:

![Learning Rate Graph](test_imgs/learning_rate.jpg)

---
  
## 🔍 Results
`Prompt: "Create a poster for a website with text 'DIGIVARSITY', background as sunset mountain college."`
![Output](test_imgs/output.png) 

`Prompt: "Print a poster with text 'CHAMPIONS LEAGUE' at the top, and 'MADRID' and 'FINAL' at the bottom."`
![Output](test_imgs/champions_league.jpg) 

## Observations
- Text Placement: The model demonstrates basic text placement but requires further refinement for complex layouts.
- Visual Quality: Image quality is high, but further training is needed to improve text stylization and integration.
  
##✨ Next Steps

- Expand training to the full dataset for better accuracy.
- Develop new loss functions to better handle text placement errors.
- Train the model for multilingual text support.
- Improve text stylization and unstructured layout handling.
- 
## 🛠️ Tools & Models
- Framework : `PyTorch`
- Image Generation: `FLUX.1-dev`
- Control Parameters: `ControlNet`
- Caption Generation: `moondream2`
- Conditional Image Generation: `Lineart`
- Text Encoding:`FLUX.1-dev-4bit`
- Unified Controlnet: `FLUX.1-dev-ControlNet-Union-Pro`
  
## 🤝 Contributing
- We welcome contributions! To contribute:
- Fork the repository.
- or Submit a pull request with your changes or suggestions.
  
## 🏆 Acknowledgements

- **[fhai50032](https://github.com/IsNoobgrammer)** for his valuable contributions to this project.
- **`Black Forest Labs`** for the **`FLUX.1-dev`** model.  
- **`lllyasviel`** for ControlNet and Annotators, which made conditional image generation possible.  
- **`vikhyatk`** for the **`moondream2`** model, enabling automated caption generation.
- **`HighCWu`** for the **`FLUX.1-dev-4bit`**.
- **`Shakker-Labs`** for **`FLUX.1-dev-ControlNet-Union-Pro`**.

---

## 📜 License

```text
Apache License 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

