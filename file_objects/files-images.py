# modes -rb (read), -wb(write)


# Copying the image starts, without chunks:
with open("bronx.jpg", "rb") as rf:
    with open("bronx_copy.jpg", "wb") as wf:
        for line in rf:
            wf.write(line)

# Copying the image with chunks:
with open("bronx.jpg", "rb") as rf:
    with open("bronx_copy.jpg", "wb") as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
