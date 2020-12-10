import sys
from PyQt5.QtWidgets import*

class MortgageCalculator(QDialog):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Mortgage Calculator")
		self.setFixedWidth(500)
		self.setFixedHeight(400)
                
		price = QLabel('Principal Price:')
		self.principalSpinBox = QDoubleSpinBox()
		self.principalSpinBox.setRange(0, 100_000_000)
		self.principalSpinBox.setPrefix('$')
		self.principalSpinBox.valueChanged.connect(self.calculate_interest)

		downPayment = QLabel('Down Payment:')
		self.downPaymentSpinBox = QDoubleSpinBox()
		self.downPaymentSpinBox.setRange(0, 100_000_000)
		self.downPaymentSpinBox.setPrefix('$')
		self.downPaymentSpinBox.valueChanged.connect(self.calculate_interest)

		rate = QLabel('Interest Rate:')
		self.rateSpinBox = QDoubleSpinBox()
		self.rateSpinBox.setRange(0, 100) 
		self.rateSpinBox.setValue(10) 
		self.rateSpinBox.setSuffix('%')
		self.rateSpinBox.valueChanged.connect(self.calculate_interest)

		year = QLabel('Number Of Years:')
		self.yearsComboBox = QComboBox()
		self.yearsComboBox.addItem('1 year')
		self.yearsComboBox.addItems(
			['{0} years'.format(year) for year in range(2, 100)]
		)
		self.yearsComboBox.currentIndexChanged.connect(self.calculate_interest)

		totalMonthly = QLabel('The Monthly Payment:')
		self.dollarLabel = QLabel()

		Layout = QGridLayout()
		Layout.addWidget(price, 0, 0)
		Layout.addWidget(self.principalSpinBox, 0, 1)
		Layout.addWidget(downPayment, 1, 0)
		Layout.addWidget(self.downPaymentSpinBox, 1, 1)
		Layout.addWidget(rate, 2, 0)
		Layout.addWidget(self.rateSpinBox, 2, 1)
		Layout.addWidget(year, 3, 0)
		Layout.addWidget(self.yearsComboBox, 3, 1)
		Layout.addWidget(totalMonthly, 4, 0)
		Layout.addWidget(self.dollarLabel, 4, 1)

		vLayout = QVBoxLayout()
		vLayout.addLayout(Layout)
		self.setLayout(vLayout)

		self.calculate_interest()

	def calculate_interest(self):
		p = self.principalSpinBox.value()
		d = self.downPaymentSpinBox.value()
		p -= d
		r = self.rateSpinBox.value()/100
		r /= 12
		y = self.yearsComboBox.currentIndex() + 1
		y *= 12
		amt = p*((r*(1+r)**y)/(((1+r)**y)-1))
		self.dollarLabel.setText('$ {0:.2f}'.format(amt))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	test = MortgageCalculator()
	test.show()

sys.exit(app.exec_())
