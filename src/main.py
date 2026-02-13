import asyncio
from agents import Runner
from src.agent import build_agent

async def main():
    agent = build_agent()

    print("🌿 Agente Mozondó iniciado. Digite sua pergunta (ou 'sair').\n")

    conversation_history = []

    while True:
        user_input = input("Você: ").strip()
        if user_input.lower() in ("sair", "exit", "quit"):
            break

        try:
            conversation_history.append(
                {"role": "user", "content": user_input}
            )

            result = await Runner.run(agent, conversation_history)

            reply = result.final_output

            print("\nMozondó:", reply, "\n")

            conversation_history.append(
                {"role": "assistant", "content": reply}
            )

        except Exception as e:
            print("\n⚠️ Erro:", str(e), "\n")

if __name__ == "__main__":
    asyncio.run(main())
