import matplotlib.pyplot as plt
import matplotlib.patches as patches


def visualize_banner_layout():
    img_width = 2000
    img_height = 1000

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))

    # Set white background
    ax.set_facecolor("white")

    # Set limits and invert Y axis so (0,0) is at the top-left (like an image)
    ax.set_xlim(0, img_width)
    ax.set_ylim(img_height, 0)

    # Format: 'Label': [Left, Top, Width, Height] (in 0.0 to 1.0 format)
    elements = [
        # --- Graphics ---
        {
            "label": "Main Visual",
            "rect": [0.56, 0.16, 0.38, 0.68],
            "color": "#f4d03f",  # Yellow
            "edgecolor": "#d4ac0d",
            "alpha": 0.7,
        },
        {
            "label": "Logo Icon",
            "rect": [0.05, 0.14, 0.06, 0.12],
            "color": "#85c1e9",  # Light Blue
            "edgecolor": "#2e86c1",
            "alpha": 0.8,
        },
        # --- Text Fields ---
        {
            "label": "Brand Name",
            "rect": [0.13, 0.15, 0.20, 0.10],
            "color": "none",
            "edgecolor": "black",
            "linestyle": "--",
        },
        {
            "label": "Headline",
            "rect": [0.07, 0.34, 0.38, 0.20],
            "color": "none",
            "edgecolor": "black",
            "linestyle": "-",
        },
        {
            "label": "Sub-headline",
            "rect": [0.07, 0.58, 0.25, 0.15],
            "color": "none",
            "edgecolor": "black",
            "linestyle": "--",
        },
        {
            "label": "Legal Disclaimer",
            "rect": [0.07, 0.82, 0.40, 0.08],
            "color": "none",
            "edgecolor": "gray",
            "linestyle": ":",
        },
    ]

    # Loop through elements and draw them
    for el in elements:
        left, t, w, h = el["rect"]

        # Convert percentages to pixels
        x_pos = left * img_width
        y_pos = t * img_height
        width_px = w * img_width
        height_px = h * img_height

        # Create rectangle patch
        rect = patches.Rectangle(
            (x_pos, y_pos),
            width_px,
            height_px,
            linewidth=2,
            edgecolor=el.get("edgecolor", "black"),
            facecolor=el.get("color", "none"),
            linestyle=el.get("linestyle", "-"),
            alpha=el.get("alpha", 1.0),
        )

        ax.add_patch(rect)

        # Add label text in the center of the box
        # Slightly offset text for smaller boxes to keep it readable
        ax.text(
            x_pos + 5,
            y_pos + 15,
            el["label"],
            fontsize=9,
            color="black",
            fontweight="bold",
            verticalalignment="top",
        )

    # Clean up chart appearance
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Banner Layout Analysis (Bounding Boxes)", fontsize=14, pad=20)

    # Add border around the whole banner
    border = patches.Rectangle(
        (0, 0), img_width, img_height, linewidth=4, edgecolor="black", facecolor="none"
    )
    ax.add_patch(border)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    visualize_banner_layout()
