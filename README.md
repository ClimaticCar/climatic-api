# Janaina Iara - API Backend (Render)

Este é o backend da aplicação, configurado para ser hospedado no Render.

## Como hospedar no Render

1. **Crie uma conta no Render**: https://render.com
2. **Conecte seu repositório GitHub** que contém estes arquivos
3. **Crie um novo Web Service**
4. **Configure as seguintes opções**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn api:app`
   - **Environment**: `Python 3`

## Arquivos inclusos

- `api.py` - API Flask principal
- `requirements.txt` - Dependências Python
- `portfolio_images/` - Pasta com todas as imagens organizadas por porte

## Estrutura de pastas de imagens

```
portfolio_images/
├── pequeno_porte/     # Imagens de pets pequenos
├── medio_porte/       # Imagens de pets médios
└── grande_porte/      # Imagens de pets grandes
```

## Como adicionar/remover imagens

1. **Para adicionar**: Coloque as imagens na pasta correspondente ao porte
2. **Para remover**: Delete as imagens da pasta
3. **Formatos suportados**: .jpg, .jpeg, .png, .gif, .webp

As mudanças são automáticas - a API detecta as imagens automaticamente.

## Endpoints da API

- `GET /api/portfolio-images` - Retorna todas as imagens organizadas por categoria
- `GET /portfolio_images/<path>` - Serve as imagens estáticas
- `GET /` - Página de teste (opcional)

## URL da API

Após o deploy no Render, sua API estará disponível em:
`https://seu-nome-do-servico.onrender.com`

**IMPORTANTE**: Anote esta URL pois você precisará atualizar o frontend com ela.

