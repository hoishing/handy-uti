from handy_uti import page_metadata


def utils_table_md():
    raw_img_base = "https://raw.githubusercontent.com/hoishing/handy-uti/main/screenshots/"
    table = "| Feature | Description | Screenshot |\n"
    table += "| --- | --- | :---: |\n"
    for page_name in page_metadata:
        image = f"{raw_img_base}{page_name}.webp"
        title = page_metadata[page_name]["title"]
        description = page_metadata[page_name]["description"]
        row = f"| {title} | {description} | [📷]({image}) |\n"
        table += row
    return table


if __name__ == "__main__":
    print(utils_table_md())
