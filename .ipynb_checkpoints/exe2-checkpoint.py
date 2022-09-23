{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c473436f",
   "metadata": {},
   "source": [
    "2 – Digite a seguinte expressão no interpretador:\n",
    "• 10 % 3 * 10 ** 2 +1 – 10 * 4 / 2\n",
    "Tente resolver o mesmo cálculo, usando apenas lápis e papel. Observe como a prioridade das\n",
    "operações é importante."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7f898fb9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "81.0"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "10 % 3 * 10 ** 2 +1-10 * 4 / 2"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f77e8022",
   "metadata": {},
   "source": [
    "O python realiza algumas operações antes das outras e modifica o resultado esperado. Precisariamos utilizar os parenteses para dar prioridade as operações. No papel teriamos a operação. No python o codigo seria = (((((10%3)*10**2)+1)-10)*4)/2 com resultado de 182 conforme segue abaixo."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4f21656b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "182.0"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(((((10%3)*10**2)+1)-10)*4)/2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
