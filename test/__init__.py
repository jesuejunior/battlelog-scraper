__author__ = 'jesuejunior'

def rebuild_schema(*metadataManagers):
    for mm in metadataManagers:
        if 'sqlite' in mm.bind.url.drivername:
            mm.drop_all()
            mm.create_all()