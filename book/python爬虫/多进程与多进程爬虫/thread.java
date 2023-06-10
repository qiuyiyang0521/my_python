请把以下Java代码转换成Python代码
public class thread {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("-----主线程开始-----");

        List<Thread> threads = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            Thread t = new Thread(() -> {
                for (int j = 0; j < 3; j++) {
                    try {
                        Thread.sleep(1000);
                        System.out.printf("Thread's name is %s\n", Thread.currentThread().getName());
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            });
            threads.add(t);
        }

        for (Thread t : threads) {
            t.start();
        }

        for (Thread t : threads) {
            t.join();
        }

        System.out.println("-----主线程结束-----");
    }
}
