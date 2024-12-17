from textwrap import dedent


def clean_text(text: str) -> str:
    return dedent(text).strip()


def header(width: int, height: int) -> str:
    return clean_text(f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
    width="{width}mm"
    height="{height}mm"
    viewBox="0 0 {width} {height}"
    version="1.1"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:svg="http://www.w3.org/2000/svg">""")


def body(width: int, height: int) -> str:
    return clean_text(f"""
        <rect
            style="fill:#ffffff;stroke:#ff0000;stroke-width:0.163087"
            id="rect1"
            width="{width}"
            height="{height}"
            x="0"
            y="0" />""")


def footer() -> str:
    return clean_text("""</svg>""")


def main():
    width = input("Please enter width(mm): ")
    height = input("Please enter height(mm): ")
    svg = header(width, height) + "\n" + body(width, height) + "\n" + footer()

    with open("output.svg", "w") as f:
        f.write(svg)


if __name__ == "__main__":
    main()
