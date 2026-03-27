#Let's imagine we have a whole EEG preprocessing script here :)
## Example Usage

This example shows how to load EEG data, plot the PSD, and save it as a TSV file using MNE-Python:

```python
import mne
import pandas as pd

# Load your EEG data (EDF file)
raw = mne.io.read_raw_edf('example_data.edf', preload=True)

# Plot Power Spectral Density (PSD)
raw.plot_psd(fmax=20)

# Convert raw data to a pandas DataFrame
df = raw.to_data_frame()

# Save as TSV
df.to_csv('eeg_data.tsv', sep='\t', index=False)
