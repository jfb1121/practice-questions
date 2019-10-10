

def honoi(no_of_disks,
          start_pole,
          end_pole,
          auxiliary_pole):

    if no_of_disks == 1:
        print(f'move {no_of_disks} from rod {start_pole} to {end_pole}')

        return

    honoi(no_of_disks - 1,
          start_pole,
          auxiliary_pole,
          end_pole)
    # print(f'move {no_of_disks} from rod {start_pole} to {end_pole}')
    honoi(1, start_pole, end_pole, auxiliary_pole)

    honoi(no_of_disks - 1,
          auxiliary_pole,
          end_pole,
          start_pole)
