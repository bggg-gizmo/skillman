"""Public business-service layer."""
ITEMS=('alpha','beta')
def version():return {'version':'1.0.0'}
def items():return {'items':list(ITEMS)}
