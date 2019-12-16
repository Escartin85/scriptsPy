import textwrap

wbsiteText = """	Learning can happend anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and faster streaming
for anytime learning. Limitless learning, limitless possibilities."""

print("No Dedent:")
print(textwrap.fill(wbsiteText))

print("Dedent:")
dedent_text = textwrap.dedent(wbsiteText).strip()
print(dedent_text)

print("Fill:")
print(textwrap.fill(dedent_text, width=50))
print(textwrap.fill(dedent_text, width=100))

print("Controlling Indent:")
print(textwrap.fill(dedent_text, initial_indent="   ", subsequent_indent="         "))

print("Shortening Text")
short = textwrap.shorten(wbsiteText, width=15, placeholder="...")
print(short)