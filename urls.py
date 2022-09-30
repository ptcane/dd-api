import static, pages, auth, mail, metrics

def static_files(filename, ext):
    file = f"{filename}.{ext}"
    
    return send_from_directory("static", file)

