import asyncio
import json

from spigetpy import r_download, r_details
async def download_by_resource_id(resource_id, directory):
    detail = await r_details(resource_id)
    name = detail["name"]
    file_type = detail["file"]["type"]
    file = await r_download(resource_id)
    try:
        with open(f"{directory}/{name}{file_type}", "wb") as f:
            f.write(file)
    except Exception as e:
        print(f"Error: {e}")
        return None
    return name


if __name__ == '__main__':
    # input resource id and directory 74429
    resource_id = input("Resource ID: ") or 74429
    # default directory is current directory
    directory = input("Directory: ") or "."
    # download resource
    task = download_by_resource_id(resource_id, directory)
    result = asyncio.run(task)
    if result:
        print(f"Downloaded {result}")
