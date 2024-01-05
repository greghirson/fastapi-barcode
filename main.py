from fastapi import FastAPI, Response

from barcode.writer import SVGWriter
from barcode import Code128
import segno
import io

app = FastAPI()

@app.get("/")
def index():
	pass

@app.get("/code128/{text}")
def code128(text: str):
	barcode_svg = Code128(text, writer = SVGWriter())
	svg = barcode_svg.render()
	return Response(content=svg, media_type="image/svg+xml")

@app.get("/qr/{text}")
def qr(text: str):
	qr = segno.make(text, micro=False)
	buffer = io.BytesIO()
	qr.save(buffer, kind='svg', scale = 4)
	buffer.seek(0)
	svg = buffer.getvalue().decode()
	return Response(svg, media_type="image/svg+xml")

