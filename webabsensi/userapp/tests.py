from django.test import TestCase
from PIL import Image, ImageDraw
import io
from .models import process_student_photo


class PhotoProcessTest(TestCase):
    def test_process_student_photo_square_and_bottom_aligned(self):
        img = Image.new("RGB", (400, 800), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.rectangle((100, 100, 300, 700), fill=(200, 50, 50))
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        res = process_student_photo(buf, size=600)
        out = Image.open(res)
        self.assertEqual(out.size, (600, 600))
        self.assertEqual(out.mode, "RGBA")
        # Subject touches bottom edge (y = 600)
        self.assertEqual(out.getbbox()[3], 600)

