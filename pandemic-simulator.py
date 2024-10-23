import tkinter



'''
Run simulation based of settings, and return simulation results
'''
def simulate (a, infection_period, s, i, r, masks, vaccine, iterations) :
    records = []

    # Adjust a value based on mask usage

    if (masks is True) :
        a = a * 0.3

    # Simulate

    for iteration in range (iterations) :
        record = []

        # Default case and recovery counts

        cases = a * s * i
        recoveries = i / infection_period

        # Calculate vaccine impact

        if (iteration > 399 and vaccine is True) :
            cases = cases * 0.1

        # Calculate new stats

        s = s - cases
        i = i + cases - recoveries
        r = r + recoveries

        # Add to record

        record.append (iteration)
        record.append (s)
        record.append (i)
        record.append (r)
        record.append (cases)
        record.append (recoveries)

        # Add record to records

        records.append (record)

    return records



'''
Return the virus name as a string
'''
def get_virus_name_text_input_as_string () :
    value = virus_name_text_input.get ()
    return value



'''
Return the infectivity setting as a float
'''
def get_infectivity_radioselect_as_float () :
    value = infectivity_radioselect_var.get ()
    value = float (value)
    return value



'''
Return the infection period setting as a float
'''
def get_infection_period_radioselect_as_float () :
    value = infection_period_radioselect_var.get ()
    value = float (value)
    return value



'''
Return the scale setting as a float
'''
def get_scale_radioselect_as_float () :
    value = scale_radioselect_var.get ()
    value = float (value)
    return value



'''
Return the iterations as an int
'''
def get_iterations_num_input_as_int () :
    value = iterations_num_input.get ()
    value = int (value)
    return value



'''
Return whether or not masks and being used
'''
def get_protections_checked_one_as_bool () :    
    if (protections_checked_one.get () == "1") :
        value = True
    else :
        value = False
    
    return value



'''
Return whether or not vaccines will be in effect
'''
def get_protections_checked_two_as_bool () :
    if (protections_checked_two.get () == "1") :
        value = True
    else :
        value = False
    
    return value



'''
Set the content of the details label
'''
def set_details_label (value) :
    details_label.configure (text = value)



'''
Show the next iteration
'''
def next_iteration_clicked () :
    global iteration_number
    global simulation_data

    # Calculate simulation input

    infectivity = get_infectivity_radioselect_as_float ()
    infection_period = get_infection_period_radioselect_as_float ()
    scale = get_scale_radioselect_as_float ()

    a = (0.00001 * infectivity) / (scale * 2)
    s = (50000 * scale) - 1
    i = 1
    r = 0

    masks = get_protections_checked_one_as_bool ()
    vaccine = get_protections_checked_two_as_bool ()
    iterations = get_iterations_num_input_as_int ()

    # If this is the first time running the simulation...

    if (iteration_number == -1) :
        # Display starting values

        initial_text = ""
        initial_text += f"Susceptible: {s}\n"
        initial_text += f"Infected: {i}\n"
        initial_text += f"Recovered: {r}"
        set_details_label (initial_text)

        # Run simulate()
        # Store to simulation_data
        simulation_data = simulate (
            a,
            infection_period,
            s,
            i,
            r,
            masks,
            vaccine,
            iterations
        )

        # Do Iteration 0 next
        iteration_number = 0

    # If this is not the first time...

    else:
        # Get the dynamic parts of the details text
        details_text_virus_name = f"{get_virus_name_text_input_as_string ()}\n"
        details_text_iteration_number = round (simulation_data[iteration_number][0] + 1)
        details_text_susceptible = round (simulation_data[iteration_number][1])
        details_text_infected = round (simulation_data[iteration_number][2]) 
        details_text_recovered = round (simulation_data[iteration_number][3])
        details_text_new_cases = round (simulation_data[iteration_number][4])
        details_text_new_recoveries = round (simulation_data[iteration_number][5])

        # Create the details text
        details_text = ""
        details_text += details_text_virus_name
        details_text += f"Iteration #{details_text_iteration_number}\n"
        details_text += f"Susceptible: {details_text_susceptible}\n"
        details_text += f"Infected: {details_text_infected}\n"
        details_text += f"Recovered: {details_text_recovered}\n"
        details_text += f"New cases: {details_text_new_cases}\n"
        details_text += f"New recoveries: {details_text_new_recoveries}"
        
        # Set the details text
        set_details_label(details_text)

        if (iteration_number == len (simulation_data) - 1) :
            # If the expected iteration_number is equal to the index of the last item in the array
            # we are on the last iteration

            print ("The simulation has now ended.")

        else:
            # We are not on the last iteration, so do the next one next
            iteration_number = iteration_number + 1



def main () :
    # ---------------------------------------------------------------------------- #
    #                                 Setup window                                 #
    # ---------------------------------------------------------------------------- #

    window = tkinter.Tk ()
    window.title ("Pandemic Simulator")
    window.geometry ("800x800")

    # ---------------------------------------------------------------------------- #
    #                                 Setup frames                                 #
    # ---------------------------------------------------------------------------- #

    left_frame = tkinter.Frame (window)
    left_frame.grid (row = 0, column = 0)

    center_frame = tkinter.Frame (window)
    center_frame.grid (row = 0, column = 1)

    right_frame = tkinter.Frame (window)
    right_frame.grid (row = 0, column = 2)

    # ---------------------------------------------------------------------------- #
    #                              Setup UI variables                              #
    # ---------------------------------------------------------------------------- #

    global virus_name_text_input
    global infectivity_radioselect_var
    global infection_period_radioselect_var
    global scale_radioselect_var
    global iterations_num_input
    global protections_checked_one
    global protections_checked_two
    global next_iteration_button
    global virus_name_label
    global details_label

    # ---------------------------------------------------------------------------- #
    #                            Other important globals                           #
    # ---------------------------------------------------------------------------- #

    global iteration_number
    global simulation_data

    iteration_number = -1
    simulation_data = []

    # ---------------------------------------------------------------------------- #
    #                                  Left frame                                  #
    # ---------------------------------------------------------------------------- #

    # -------------------------------- help_label -------------------------------- #

    # Setup label text

    help_label_text = "Each iteration is comparable to a day, so please only type "
    help_label_text += " positive integers greater than 3. \n\n"
    help_label_text += "Also, please ensure that you have the settings you want before "
    help_label_text += "clicking next iteration for the first time. Changing the settings "
    help_label_text += "afterwards shall have no effect."

    # Add and position label

    help_label = tkinter.Label (
        left_frame,
        text = help_label_text,
        wraplength = 200,
        relief = "sunken"
    )
    help_label.grid (row = 0, column = 0)

    # ---------------------------------------------------------------------------- #
    #                                 Center frame                                 #
    # ---------------------------------------------------------------------------- #

    # --------------------------- virus_name_text_input -------------------------- #

    # Add and position input's label

    virus_name_text_input_label = tkinter.Label (center_frame, text = "Virus name", relief = "sunken")
    virus_name_text_input_label.grid (row = 0, column = 0)

    # Add and position input

    virus_name_text_input = tkinter.Entry (
        center_frame,
        width = 15
    )
    virus_name_text_input.grid (row = 0, column = 1)

    # -------------------------- infectivity_radioselect ------------------------- #

    # Setup radioselect's variable

    infectivity_radioselect_var = tkinter.StringVar ()

    # Setup radioselect's label

    infectivity_radioselect_label = tkinter.Label (center_frame, text = "Infectivity", relief = "sunken")
    infectivity_radioselect_label.grid (row = 1, column = 0)

    # Setup radioselects

    infectivity_radioselect_one = tkinter.Radiobutton (
        center_frame,
        text = "1.0x",
        value = "1.0",
        variable = infectivity_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    infectivity_radioselect_one.grid (row = 2, column = 1)

    infectivity_radioselect_two = tkinter.Radiobutton (
        center_frame,
        text = "1.25x",
        value = "1.25",
        variable = infectivity_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    infectivity_radioselect_two.grid (row = 3, column = 1)

    infectivity_radioselect_three = tkinter.Radiobutton (
        center_frame,
        text = "1.5x",
        value = "1.5",
        variable = infectivity_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    infectivity_radioselect_three.grid (row = 4, column = 1)

    infectivity_radioselect_four = tkinter.Radiobutton (
        center_frame,
        text = "1.75x",
        value = "1.75",
        variable = infectivity_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    infectivity_radioselect_four.grid (row = 5, column = 1)

    infectivity_radioselect_five = tkinter.Radiobutton (
        center_frame,
        text = "2.0x",
        value = "2.0",
        variable = infectivity_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    infectivity_radioselect_five.grid (row = 6, column = 1)

    # Set the first radioselect as the default

    infectivity_radioselect_one.invoke ()

    # ----------------------- infection_period_radioselect ----------------------- #

    # Setup radioselect's variable

    infection_period_radioselect_var = tkinter.StringVar ()

    # Setup radioselect's label

    infection_period_radioselect_label = tkinter.Label (
        center_frame,
        text = "Infection period",
        relief = "sunken"
    )
    infection_period_radioselect_label.grid (row = 7, column = 0)

    # Setup radioselects

    infection_period_radioselect_one = tkinter.Radiobutton (
        center_frame,
        text = "3 days",
        value = "3",
        variable = infection_period_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    infection_period_radioselect_one.grid (row = 8, column = 1)

    infection_period_radioselect_two = tkinter.Radiobutton (
        center_frame,
        text = "7 days",
        value = "7",
        variable = infection_period_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    infection_period_radioselect_two.grid (row = 9, column = 1)

    infection_period_radioselect_three = tkinter.Radiobutton (
        center_frame,
        text = "14 days",
        value = "14",
        variable = infection_period_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    infection_period_radioselect_three.grid (row = 10, column = 1)

    infection_period_radioselect_four = tkinter.Radiobutton (
        center_frame,
        text = "28 days",
        value = "28",
        variable = infection_period_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    infection_period_radioselect_four.grid (row = 11, column = 1)

    # Set second radioselect as default

    infection_period_radioselect_two.invoke ()

    # ----------------------------- scale_radioselect ---------------------------- #

    # Setup radioselect's variable

    scale_radioselect_var = tkinter.StringVar ()

    # Setup radioselect's label

    scale_radioselect_label = tkinter.Label (
        center_frame,
        text = "Scale",
        relief = "sunken"
    )
    scale_radioselect_label.grid (row = 12, column = 0)

    # Setup radioselects

    scale_radioselect_one = tkinter.Radiobutton (
        center_frame,
        text = "Town",
        value = "1",
        variable = scale_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    scale_radioselect_one.grid (row = 13, column = 1)

    scale_radioselect_two = tkinter.Radiobutton (
        center_frame,
        text = "City",
        value = "10",
        variable = scale_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    scale_radioselect_two.grid (row = 14, column = 1)

    scale_radioselect_three = tkinter.Radiobutton (
        center_frame,
        text = "Country",
        value = "1000",
        variable = scale_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    scale_radioselect_three.grid (row = 15, column = 1)

    scale_radioselect_four = tkinter.Radiobutton (
        center_frame,
        text = "Continent",
        value = "10000",
        variable = scale_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    scale_radioselect_four.grid (row = 16, column = 1)

    scale_radioselect_five = tkinter.Radiobutton (
        center_frame,
        text = "World",
        value = "100000",
        variable = scale_radioselect_var,
        relief = "raised",
        width = 15,
        anchor = "w"
    )
    scale_radioselect_five.grid (row = 17, column = 1)

    # Set third radioselect as default

    scale_radioselect_three.invoke ()

    # --------------------------- iterations_num_input --------------------------- #

    # Set input's label

    iterations_num_input_label = tkinter.Label (
        center_frame,
        text = "Iterations",
        relief = "sunken"
    )
    iterations_num_input_label.grid (row = 18, column = 0)

    # Add and position input

    iterations_num_input = tkinter.Entry (
        center_frame,
        width = 15,
    )
    iterations_num_input.grid (row = 18, column = 1)

    # --------------------------- protections_checklist -------------------------- #

    # Setup checkboxes' variables

    protections_checked_one = tkinter.StringVar ()
    protections_checked_two = tkinter.StringVar ()

    # Setup checkboxes' label

    protections_checklist_label = tkinter.Label (
        center_frame, 
        text = "Protections",
        relief = "sunken"
    )
    protections_checklist_label.grid (row = 19, column = 0)

    # Add and position first checkbox

    protections_checklist_one = tkinter.Checkbutton (
        center_frame,
        text = "Mask usage",
        variable = protections_checked_one,
        relief = "raised",
        width = 25,
        anchor = "w"
    )
    protections_checklist_one.grid (row = 20, column = 1)

    # Add and position second checkbox

    protections_checklist_two = tkinter.Checkbutton (
        center_frame,
        text = "Vaccines (after iteration 400)",
        variable = protections_checked_two,
        relief = "raised",
        width = 25,
        anchor = "w"
    )
    protections_checklist_two.grid (row = 21, column = 1)

    # Check both of them by default

    protections_checklist_one.invoke ()
    protections_checklist_two.invoke ()

    # ---------------------------------------------------------------------------- #
    #                                  Right frame                                 #
    # ---------------------------------------------------------------------------- #

    # ----------------------------- virus_name_label ----------------------------- #

    # --------------------------- next_iteration_button -------------------------- #

    next_iteration_button = tkinter.Button (
        right_frame,
        text = "Next iteration",
        command = next_iteration_clicked
    )
    next_iteration_button.grid (row = 0, column = 0)

    # ------------------------------- details_label ------------------------------ #

    details_label = tkinter.Label (
        right_frame,
        text = "Get started by clicking next iteration, to see the initial data.",
        wraplength = 250,
        relief = "sunken"
    )
    details_label.grid (row = 1, column = 0)

    # ---------------------------------------------------------------------------- #
    #                            Make window interactive                           #
    # ---------------------------------------------------------------------------- #

    window.mainloop ()



main ()