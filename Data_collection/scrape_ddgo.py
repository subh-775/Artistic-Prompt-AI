import os
import aiohttp
import asyncio
import requests
from tqdm import tqdm
from duckduckgo_search import DDGS

# Define the keywords_dict with Indian specific keywords
keywords_dict = {
    "Sale Flyers & Promotions": [
        "Diwali sale flyers",
        "New Year sale posters",
        "Navratri sale promotions",
        "Republic Day sale brochures",
        "Durga Puja sale flyers",
        "Eid festival sale flyers",
        "Pongal sale posters",
        "Onam sale flyers",
        "Gudi Padwa sale ads",
        "Makar Sankranti sale brochures",
        "flash sale flyers India",
        "seasonal discount flyers India"
    ],
    "College Pamphlets & Admission Brochures": [
        "college admission pamphlets India",
        "university brochures India",
        "engineering college flyers",
        "MBA admission flyers India",
        "school admission brochures India",
        "open day flyers India",
        "college event posters India",
        "education fair brochures India"
    ],
    "Festival Sales & Event Flyers": [
        "Diwali sale posters",
        "Holi festival sale flyers",
        "Christmas sale posters India",
        "Eid sale flyers India",
        "Baisakhi sale posters",
        "Makar Sankranti flyers",
        "Pongal celebration flyers",
        "Durga Puja festival promotions",
        "Dussehra sale flyers"
    ],
    "Event Organization Notices & Flyers": [
        "event management flyers India",
        "wedding invitation flyers India",
        "concert posters India",
        "cultural event flyers",
        "college fest posters",
        "corporate event flyers India",
        "charity event posters India"
    ],
    "Festival Greetings & Wishes Posters": [
        "Diwali greeting posters",
        "Holi wishes flyers",
        "Eid greeting posters India",
        "New Year wishes flyers India",
        "Onam greeting posters",
        "Pongal wishes flyers",
        "Baisakhi celebration posters"
    ],
    "General Flyers & Notices": [
        "community event flyers India",
        "public awareness flyers India",
        "local event posters India",
        "government notice flyers",
        "exhibition posters India",
        "public health campaign flyers"
    ],
    "Educational Flyers & Brochures": [
        "school brochures India",
        "educational program flyers",
        "tuitions and coaching center flyers",
        "vocational training brochures",
        "seminar event flyers India",
        "college festival brochures"
    ],
    "Miscellaneous Promotion Posters": [
        "business launch flyers India",
        "promotional offers posters India",
        "shop opening flyers India",
        "special discount flyers India",
        "new product launch promotions"
    ]
}

# Function to download images asynchronously
async def download_image(session, url, folder, idx):
    retries = 3
    for attempt in range(retries):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    # Write the image to a file
                    image_data = await response.read()
                    with open(os.path.join(folder, f"{idx}.jpg"), "wb") as img_file:
                        img_file.write(image_data)
                    # print(f"Downloaded: {folder}/{idx}.jpg")
                    return
                else:
                    # print(f"Failed to download {url}. Status code: {response.status}")
                    pass
        except Exception as e:
            # print(f"Attempt {attempt + 1} failed for {url}. Error: {e}")
            pass
    print(f"Failed to download {url} after {retries} attempts.")

async def fetch_and_download_images(keywords):
    for keyword in keywords:
        # Create a directory for the keyword
        folder = keyword.replace(" ", "_")
        os.makedirs(folder, exist_ok=True)

        # Fetch images using DDGS
        results = DDGS().images(
            keywords=keyword,
            region="in-en",
            safesearch="on",
            color="color",
            type_image="photo",
            max_results=50,  # You can increase this number as needed
        )

        async with aiohttp.ClientSession() as session:
            # Download images asynchronously
            tasks = []
            for idx, result in enumerate(results):
                image_url = result.get("image")
                if image_url:
                    tasks.append(download_image(session, image_url, folder, idx + 1))

            # Monitor progress
            for task in tqdm(asyncio.as_completed(tasks), total=len(tasks)):
                await task

# Main function to run the script
def main():
    # Flatten the keywords_dict to get a list of all keywords
    all_keywords = [keyword for keywords in keywords_dict.values() for keyword in keywords]
    
    asyncio.run(fetch_and_download_images(all_keywords))

if __name__ == "__main__":
    main()
