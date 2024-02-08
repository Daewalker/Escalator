def get_cust_input():
    customer_name = input("Please enter customer name (type 'exit' to exit): ")
    return customer_name
  
def escalate_customer(customer_name):
    # Defines escalation path based on customer that was input
    escalation_paths = {
        'xci': 'Escalate to XCI-Support',
        'igt': 'Escalate to ___',
        'hdb': 'Escalate to ___',
        'shz': 'Escalate to ENE 886386',
        'shs': 'Escalate to ENE 886386',
        'deg': 'Escalate to ENE 886386',
        'hfa': 'Escalate to ENE 886386',
        'shp': 'Escalate to ENE 886386',
        'shy': 'Escalate to ENE 886386',
        'doc': 'Escalate to ENE 886386',
        'usps': 'Escalate to ENE 886386',
        'azd': 'Escalate to ENE 886386',
        'mcd': 'Escalate to ENE 886386',
        'pil': 'Escalate to ENE 886386',
        'agd': 'Escalate to ENE 886386',
        'ctn': 'Escalate to ENE 886386',
        'cop': 'Escalate to ENE 886386',
        'qck': 'Escalate to ENE 886386',
        'wvg': 'Escalate to ENE 886386',
        'hfe': 'Escalate to ENE 886386',
        'vsc': 'Escalate to ENE 886386',
        'ncp': 'Escalate to ENE 886386',
        'iseycocnt': 'Escalate to ENE 886386',
        'aac': 'reach out to Ajit, Murugan or Sampath',
        'aad': 'reach out to Ajit, Murugan or Sampath',
        'ags': 'reach out to Ajit, Murugan or Sampath',
        'ait': 'reach out to Ajit, Murugan or Sampath',
        'ant': 'reach out to Ajit, Murugan or Sampath',
        'apd': 'reach out to Ajit, Murugan or Sampath',
        'atc': 'reach out to Ajit, Murugan or Sampath',
        'azd': 'reach out to Ajit, Murugan or Sampath',
        'bbg': 'reach out to Ajit, Murugan or Sampath',
        'blm': 'reach out to Ajit, Murugan or Sampath',
        'bmg': 'reach out to Ajit, Murugan or Sampath',
        'brn': 'reach out to Ajit, Murugan or Sampath',
        'bsk': 'reach out to Ajit, Murugan or Sampath',
        'ccc': 'reach out to Ajit, Murugan or Sampath',
        'cdd': 'reach out to Ajit, Murugan or Sampath',
        'cfn': 'reach out to Ajit, Murugan or Sampath',
        'cly': 'reach out to Ajit, Murugan or Sampath',
        'com': 'reach out to Ajit, Murugan or Sampath',
        'csy': 'reach out to Ajit, Murugan or Sampath',
        'ctn': 'reach out to Ajit, Murugan or Sampath',
        'dak': 'reach out to Ajit, Murugan or Sampath',
        'dti': 'reach out to Ajit, Murugan or Sampath',
        'ecc': 'reach out to Ajit, Murugan or Sampath',
        'ene/eed': 'reach out to Ajit, Murugan or Sampath',
        'eps': 'reach out to Ajit, Murugan or Sampath',
        'erc': 'reach out to Ajit, Murugan or Sampath',
        'fdx': 'reach out to Ajit, Murugan or Sampath',
        'fef': 'reach out to Ajit, Murugan or Sampath',
        'fla': 'reach out to Ajit, Murugan or Sampath',
        'fsa': 'reach out to Ajit, Murugan or Sampath',
        'gcd': 'reach out to Ajit, Murugan or Sampath',
        'gds': 'reach out to Ajit, Murugan or Sampath',
        'gsa': 'reach out to Ajit, Murugan or Sampath',
        'gtv': 'reach out to Ajit, Murugan or Sampath',
        'hkf': 'reach out to Ajit, Murugan or Sampath',
        'ibg': 'reach out to Ajit, Murugan or Sampath',
        'ine': 'reach out to Ajit, Murugan or Sampath',
        'jag': 'reach out to Ajit, Murugan or Sampath',
        'kew': 'reach out to Ajit, Murugan or Sampath',
        'mcd': 'reach out to Ajit, Murugan or Sampath',
        'nbs': 'reach out to Ajit, Murugan or Sampath',
        'ntf': 'reach out to Ajit, Murugan or Sampath',
        'ofh': 'reach out to Ajit, Murugan or Sampath',
        'pba': 'reach out to Ajit, Murugan or Sampath',
        'pci': 'reach out to Ajit, Murugan or Sampath',
        'peg': 'reach out to Ajit, Murugan or Sampath',
        'ppt': 'reach out to Ajit, Murugan or Sampath',
        'rdd': 'reach out to Ajit, Murugan or Sampath',
        'rec': 'reach out to Ajit, Murugan or Sampath',
        'rmw': 'reach out to Ajit, Murugan or Sampath',
        'sed': 'reach out to Ajit, Murugan or Sampath',
        'sma': 'reach out to Ajit, Murugan or Sampath',
        'smr': 'reach out to Ajit, Murugan or Sampath',
        'ssb': 'reach out to Ajit, Murugan or Sampath',
        'stg': 'reach out to Ajit, Murugan or Sampath',
        'tdr': 'reach out to Ajit, Murugan or Sampath',
        'tep': 'reach out to Ajit, Murugan or Sampath',
        'upl': 'reach out to Ajit, Murugan or Sampath',
        'upr': 'reach out to Ajit, Murugan or Sampath',
        'wfs': 'reach out to Ajit, Murugan or Sampath',
        'gcm': ' Gateway control modulator = CNE-GW 884140(Primary) or 884141(Secondary)',
        '': '',
        # Add more as the list grows
    }
    
    # Start loop
    if customer_name.lower() == 'exit':
        return False    # exit the loop
    
    if customer_name.lower() in escalation_paths:
        escalation_path = escalation_paths[customer_name.lower()]
        print(f"\nEscalation path for {customer_name}: is {escalation_path}\n")
    else:
        print(f"No escalation path found for {customer_name}. Follow up with other techs.")
        
    return True # continue the loop
    
def display_banner():
    banner = """
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    *       Customer Escalation Tool     *
    *         Created for the NMC        *
    *~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*
    """
    print(banner)
    
def main():
    display_banner()
    
    while True:
        customer_name = get_cust_input()
        if not escalate_customer(customer_name):
            break   # Breaks the loop when 'exit' is typed

if __name__ == "__main__":
    main()
