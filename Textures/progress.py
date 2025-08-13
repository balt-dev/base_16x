from pathlib import Path
from PIL import Image

def main():
	total_count = 0
	small_count = 0
	for path in Path(".").rglob("*.png"):
		if "Layers" in f"{path}": continue
		with Image.open(path) as im:
			total_count += 1
			if im.width <= 32 and im.height <= 32:
				small_count += 1
	print(f"{(small_count / total_count * 100):.2f}% done ({small_count} / {total_count})")

if __name__ == "__main__":
	main()