
import argparse as ap
import os
import shutil

from csl_pipeline.config import JHOLT_HOME

PIPELINE_RESULTS_FOLDER = f'{JHOLT_HOME}/CSL_pipeline_benchmark/results'
PUBLIC_RESULTS_FOLDER = f'{JHOLT_HOME}/CSL_public_benchmark/results'

if __name__ == '__main__':
    #first set up the arg parser
    DESC="Wrapper script copying over results from the main pipeline"
    p = ap.ArgumentParser(description=DESC, formatter_class=ap.RawTextHelpFormatter)
    
    #optional arguments with default
    
    #required main arguments
    p.add_argument('new_date', type=str, help='the data files to copy')
    
    #parse the arguments
    args = p.parse_args()

    new_date = args.new_date

    #make the folder
    date_folder = f'{PUBLIC_RESULTS_FOLDER}/{new_date}'
    if not os.path.exists(date_folder):
        os.makedirs(date_folder)

    #then copy in the results PDF...
    in_pdf = f'{PIPELINE_RESULTS_FOLDER}/results_{new_date}_results.pdf'
    out_pdf = f'{date_folder}/results_{new_date}.pdf'
    shutil.copy(in_pdf, out_pdf)

    #... and the CSV file
    in_csv = f'{PIPELINE_RESULTS_FOLDER}/results_{new_date}_csv/small_summary.csv'
    out_csv = f'{date_folder}/small_summary_{new_date}.csv'
    shutil.copy(in_csv, out_csv)
