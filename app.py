import streamlit as st

def image_function():
    x = input("Digite o nome: ")  # Solicita a entrada do usuário diretamente
    if x == 'Daiany':
        return "Mais linda de todas"
    else:
        return "Muito feia"

def main():
    st.write(image_function())

if __name__ == '__main__':
    main()