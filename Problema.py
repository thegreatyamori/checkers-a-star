class Problema(object):
  def __init__(self, estado_inicial, estado_final = None):
    self.estado_inicial = estado_inicial
    self.estado_final = estado_final

  def acciones(self, estado):
    pass

  def aplica(self, estado, accion):
    pass

  def isFinalState(self, estado):
    return estado == self.estado_final

  def coste_aplicar_accion(self, estado, accion):
    return 1