from jnius import autoclass
autoclass('java.lang.System').out.println('Hello World!')
