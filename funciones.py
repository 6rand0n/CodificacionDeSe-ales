def filtrar(event, text_widget):
    
    # Permitir teclas de edición
    if event.keysym in ("BackSpace", "Delete", "Left", "Right", "Up", "Down"):
        return  # Permitir estas teclas

    # Permitir solo 0 y 1
    if event.char not in ("0", "1"):
        return "break"  # Cancela cualquier otro carácter
    
    text_widget.tag_add("centrado", "1.0", "end")
    contenido = text_widget.get("1.0", "end-1c")