from search.nim import NimAgent, Nim, NimGameplay, MinimaxNimAgent, even_total_discs_function


if __name__ == '__main__':
    nim: Nim = Nim(5)
    nim_agent: NimAgent = MinimaxNimAgent(nim_start=nim, limit=5)
    print('Result: ' + NimGameplay.gameplay(nim, nim_agent, even_total_discs_function))
    # nim_agent.search_agent(True, None, False)
