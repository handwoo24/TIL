interface AbstratcFactory{
    createExamA(): AbstractExamA;

    createExamB(): AbstratcExamB;
}

class ConcreteFactory1 implements AbstratcFactory{
    public createExamA(): AbstractExamA {
        return new ConcreteExamA1();
    }

    public createExamB(): AbstractExamB {
        return new ConcreteExamB1();
    }
}

class ConcreteFactory2 implements AbstratcFactory {
    public createExamA(): AbstractExamA {
        return new ConcreteExamA2();
    }

    public createExamB(): AbstractExamB {
        return new ConcreteExamB2();
    }
}

interface AbstractExamA {
    usefulFunctionA(): string;
}

class ConcreteExamA1 implements AbstractExamA {
    public usefulFunctionA(): string {
        return 'The result of the product A1.';
    }
}

class ConcreteExamA2 implements AbstractExamA {
    public usefulFunctionA(): string {
        return 'The result of the product A2.';
    }
}
