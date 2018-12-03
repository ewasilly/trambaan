i = 1
  while i < nr_of_trajects:
      # generate a random number to use as starting connection in Traject
      start = random.choice(range(length))
      traject = Traject(connections[start])
      # # Prevent going back and forth by keeping track of used connections
      # used = []
      tried = 1
      while traject.total_time <= 120:
          # modulo is used to prevent "index out of range list" error.
          j = random.choice(numbers)
          index = j % length
          # using the Traject method add_connection, to add the connection at [j] in all_connections
          if connections[index] not in traject.connections:
              traject.add_connection(connections[index])
              tried += 1
          # if every connection has been tried:
          if tried == length:
              # if the total time of the current traject overceeds min_time use this traject.
              if traject.total_time >= min_time:
                  trajects[f"Traject {i}."] = (traject, traject.total_time)
                  total_minutes.append(traject.total_time)
                  i += 1
                  # add connections in this traject to used_all, eventually the use through all 7 trajects will be counted
                  for conn in traject.connections:
                      used_all.append(conn)
                      if conn in critical_connections:
                          used_critical.append(conn)
                  break
              # if the traject is too short, start over.
              else:
                  break
