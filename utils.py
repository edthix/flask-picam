def generate_filename(filetype='', folder='images'):
    '''
    Generate a timestamped filename
    filetype = jpg, gif, etc.
    '''
    filename = 'static/' + folder + '/image-' + time.strftime("%Y%m%d%H%M%S", time.gmtime()) + '.' + filetype
    return filename
