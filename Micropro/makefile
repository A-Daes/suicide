TARGET= myWindow
all: $(TARGET)

$(TARGET): $(TARGET).o
	g++ -ggdb $(TARGET).o `pkg-config --cflags --libs opencv` -o $(TARGET)
	rm $(TARGET).o

$(TARGET).o:
	g++ -ggdb -c $(TARGET).cpp

clean:
	rm $(TARGET).o $(TARGET)
