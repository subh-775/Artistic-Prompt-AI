# 🎨 AI-Powered Poster Generator

We are designing a machine learning model capable of generating images that **accurately incorporate specified text or lettering within the image**. Existing image-generating models often struggle with proper text placement, either misplacing the text or introducing spelling errors. Our goal is to train the model to master the art of **placing text accurately and aesthetically within generated images**. Once accomplished, this innovation will enable seamless creation of visually appealing outputs such as **poster designs** and **template fills**, all from a single prompt.

---

## 🚀 Motivation

Despite advancements in AI image generation, there are currently **no large language models (LLMs)** or image-generating models capable of achieving perfect text placement in images like movie posters. Existing models often:
- Make **mistakes in text placement**, leading to poor visual aesthetics.
- or Introduce **spelling or formatting errors** in the text.  

Our project tackles these challenges by combining **state-of-the-art AI models** and a carefully curated training pipeline to develop a model that excels in:
1. Generating high-quality images.
2. Accurately placing text in unstructured, visually appealing ways.
3. Maintaining spelling and stylistic integrity.

---

## ⚙️ Approach

### 1. **🎥 Image Generation**
We will use **[black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)** model for **image generation**. This serves as the foundation for creating visually stunning movie poster-like images.

### 2. **🔧 Conditional Image Control**
To control the image parameters (such as Resolution, Strength, DDIM sampling, seed, etc.), we use the **[lllyasviel/ControlNet](https://github.com/lllyasviel/ControlNet)** framework. ControlNet ensures that the AI understands the layout constraints required for text Understanding.

### 3. **🛠️ Data Collection and Preprocessing**
We curated our dataset using the following steps:
- **Data Collection**: Extracted thousands of movie poster images from various sources using techniques like search and web scraping and performed operations like removal of outliers, null entries and  invalid image.
- **Captions Generation**: Captions were automatically generated for each image using the **[vikhyatk/moondream2](https://huggingface.co/vikhyatk/moondream2)** model, which provided detailed descriptions of the posters.
- **Conditional Images**: We generated lineart-style conditional images for each poster using the **[lllyasviel/ControlNet-v1-1-nightly](https://github.com/lllyasviel/ControlNet-v1-1-nightly/blob/main/README.md#controlnet-11-lineart)** model. These conditional images will play a key role during training by guiding the AI on text placement.
- **Final Dataset**: <a href="https://huggingface.co/datasets/Subh775/Conditional_Movies_Poster_Dataset">Here</a> is the Final dataset so formed.

### 4. **🧠 Model Training**
Our AI model will:
- Learn to generate images using the **FLUX.1-dev** model.
- Learn text placement from the conditional lineart images and captions.
- Optimize visual text styling and accuracy through advanced training techniques.

  > **Note**: Training is not yet done. An information regarding weights and biases will be added as development continues.


---

## 📈 Current Progress

So far, we have:
1. Extracted a large dataset of movie posters.
2. Generated detailed captions for each poster using **moondream2**.
3. Created lineart-style conditional images using **lllyasviel/Annotators** **ControlNet 1.1**.

### Dataset Structure:
| **🖼️ image**         | **✍️ caption**                                                                 | **🖊️ conditional image**      |
|-----------------------|-----------------------------------------------------------------------------|-------------------------------|
| Movie poster image    | A description of the poster, including characters, text, colors, etc.      | Lineart representation        |

---

## 🔮 Next Steps

1. Train the model on the curated dataset to learn accurate text placement and styling.
2. Fine-tune the AI to ensure it handles unstructured text formats with high precision.
3. Optimize the AI for generating movie-poster-like images based on user-defined prompts.
   
---

## 🛠️ Tools & Frameworks

- **Image Generation**: [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)  
- **Control Parameters**: [ControlNet](https://github.com/lllyasviel/ControlNet)  
- **Caption Generation**: [moondream2](https://huggingface.co/vikhyatk/moondream2)  
- **Conditional Image Generation**: [Annotators](https://github.com/lllyasviel/ControlNet-v1-1-nightly/blob/main/README.md#controlnet-11-lineart)

---

## 🤝 Contributing

This project is a work in progress. Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Submit a pull request with your changes or suggestions.

---

## 🔗 More Information

More information about the project is available at  [**subh-775**](https://huggingface.co/Subh775) and [**fhai50032**](https://huggingface.co/fhai50032).

---

## 🏆 Acknowledgements

Special thanks to:
- **[fhai50032](https://github.com/IsNoobgrammer)** for his valuable contributions to this project.
- **Black Forest Labs** for the **FLUX.1-dev** model.  
- **lllyasviel** for ControlNet and Annotators, which made conditional image generation possible.  
- **vikhyatk** for the **moondream2** model, enabling automated caption generation.

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
```

> **Note**: Training and further refinements are in progress. Updates will be added as development continues.
