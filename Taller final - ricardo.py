def ver_sala():  
  for f in sala :
      print("", end="")
      for c in f:
         print("{:4}".format(c), end='')
    else:
        print(f"{Fore.RED}La sala {numero_sala} no existe.{Style.RESET_ALL}")