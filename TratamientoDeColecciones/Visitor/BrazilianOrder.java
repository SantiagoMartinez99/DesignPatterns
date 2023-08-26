public class BrazilianOrder implements Order {

    private double orderAmount;

    public BrazilianOrder() {
    }

    public BrazilianOrder(double inp_orderAmount) {
        orderAmount = inp_orderAmount;
    }

    public double getOrderAmount() {
        return orderAmount;
    }

    public void accept(OrderVisitor v) {
        v.visit(this);
    }

}
