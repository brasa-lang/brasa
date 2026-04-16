# What is Brasa?

Brasa is an interpreted programming language written in Python. By utilizing Portuguese-based syntax, it provides a natural and intuitive learning curve for native speakers and children who may find the English-centric nature of traditional coding (like C++ or Java) intimidating.

Look at the a basic program written in Brasa

## Brasa Docs

For a deep dive into Brasa philosophy and full syntax, visit the [Official Documentation](https://brasa-lang.github.io/).

## ⚡ Quick look

```
// example.brasa

diga("Digite seu nome: ");
texto nome := leia();

func bem_vindo(texto nome)->texto{
  retorne "Bem vindo, " + nome + "!";
}

texto mensagem := bem_vindo(nome);

diga(mensagem);
```

For a brief introduction, see [overview](https://brasa-lang.github.io/overview/)

## 🚀 Getting Started

Brasa is built with [Python](https://www.python.org/downloads/) and can be installed via pip

```
pip install brasa-lang
```

For detailed instructions, see [installation guide](https://brasa-lang.github.io/tutorial/getting-started/installation/)
